import { createSelector } from 'reselect';

/**
 * Direct selector to the newReview state domain
 */
const selectNewReviewDomain = () => (state) => state.get('newReview');

/**
 * Other specific selectors
 */


/**
 * Default selector used by NewReview
 */

const makeSelectNewReview = () => createSelector(
  selectNewReviewDomain(),
  (substate) => substate.toJS()
);

export default makeSelectNewReview;
export {
  selectNewReviewDomain,
};
