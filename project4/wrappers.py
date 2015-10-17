from sklearn.metrics.scorer import check_scoring
from sklearn.base import BaseEstimator, is_classifier
from sklearn.cross_validation import _check_cv as check_cv
from Queue import PriorityQueue
import numpy as np
class WrapperBase(BaseEstimator):
	def __init__(self, estimator, cv=None, scoring=None, best_subset=None):
		self._open = []
		self._closed = []
		self.scores_ = {}
		self.estimator = estimator
		self.best_subset = best_subset
		self.best_subset_score = 0
		self.scoring = scoring
		self.cv = cv
		

	def fit(self,X,Y):
		if not self.best_subset:
			self.fshape = np.shape(X)[1]
			self.scorer_ = check_scoring(self.estimator, scoring=self.scoring)

			self.cv = check_cv(self.cv, X, Y, classifier=is_classifier(self.estimator))

			self.best_subset = tuple()
			self.best_subset_score = 0
			self.scores_ = {self.best_subset:self.best_subset_score}
			X = np.array(X)
			Y = np.array(Y)


			try:
				self.get_best_subset(X,Y)
			except KeyboardInterrupt:
				pass
		self.estimator = self.estimator.fit(X[:,self.best_subset],Y)
		return self

	def predict(self,X):
		return self.estimator.predict(X[:,list(self.best_subset)])
	def get_best_subset(self, X, Y):
		raise UnimplementedException
	def evaluate_subset(self, subset, X, Y):
		if subset in self.scores_:
			return np.mean(self.scores_[subset])
		score = []

		for train,valid in self.cv:
			T,YT = X[train][:,subset], Y[train]
			V,YV = X[valid][:,subset], Y[valid]


			estimator = self.estimator.fit(T,YT)
			score.append(self.scorer_(estimator,V,YV))


			

		self.scores_[tuple(subset)] = score
		return np.mean(score)

class RandomSubsetsWrapper(WrapperBase):
	def __init__(self, estimator, cv=None, scoring=None, best_subset=None):
		super(RandomSubsetsWrapper, self).__init__(estimator=estimator, cv=cv, scoring=scoring, best_subset=best_subset)
	
	def get_best_subset(self, X, Y):
		all_pos = range(1,2**self.fshape)

		while all_pos:
			s_int = all_pos.pop(np.random.randint(len(all_pos)))
			subset = tuple(np.nonzero([int(x) for x in bin(s_int)[2:]])[0])

			score = self.evaluate_subset(subset, X, Y)

			if ( score > self.best_subset_score ) or \
						(score == self.best_subset_score and \
							len(subset) < len(self.best_subset)) :

				self.best_subset = subset
				self.best_subset_score = score
				print 'New best score:', score



	

class HillClimingWrapper(WrapperBase):
	
	def __init__(self,estimator,cv=None, scoring=None, best_subset=None):
		super(HillClimingWrapper, self).__init__(estimator, cv=cv, scoring=scoring, best_subset=best_subset)
	
	def expand(self, node):
		self.node_children_ = []

		node_list = list(node)
		# add
		for i in range(self.fshape):
			if i in node_list:
				continue
			cand = tuple(node_list + [i])
			if not cand in self.scores_:
				self.node_children_.append(cand)

		# delete
		for i in range(len(node_list)):
			cand = tuple(node_list[:i] + node_list[i+1:])
			if not cand in self.scores_:
				self.node_children_.append(cand)

		return self.node_children_


	def get_best_subset(self, X, Y):
		while True:
			best_child_score, best_child = max([(self.evaluate_subset(u, X, Y),u) for u in self.expand(self.best_subset)])
			if best_child_score <= self.best_subset_score:
				break
			else:
				self.best_subset = best_child
				self.best_subset_score = best_child_score

		return self.best_subset

class BestFirstSearchWrapper(HillClimingWrapper):
	def __init__(self, estimator, epsilon=0.01, stale_limit=30, cv=None, scoring=None, initial_subset=None, best_subset=None):
		self.epsilon = epsilon
		self.stale_limit = stale_limit
		self.initial_subset = initial_subset
		super(BestFirstSearchWrapper, self).__init__(estimator, cv=cv, scoring=scoring, best_subset=best_subset)

	def get_best_subset(self, X, Y):
		OPEN = PriorityQueue()
		if self.initial_subset is not None:
			i = self.initial_subset
			OPEN.put((-self.evaluate_subset(i,X,Y),i))
		else:
			OPEN.put((0,tuple()))

		stale_count = 0

		while stale_count < self.stale_limit and not OPEN.empty():
			score_v, v = OPEN.get() #gets max

			if score_v + self.epsilon < self.best_subset_score:
				self.best_subset_score = score_v
				self.best_subset = v
				print 'New best score:', score_v
				stale_count = 0
			else:
				stale_count +=1

			for child in self.expand(v):
				OPEN.put((-self.evaluate_subset(child,X,Y),child))


