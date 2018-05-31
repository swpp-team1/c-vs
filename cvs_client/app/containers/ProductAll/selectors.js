import { createSelector } from 'reselect';

/**
 * Direct selector to the productAll state domain
 */
const selectProductAllDomain = () => (state) => state.get('productAll');

/**
 * Other specific selectors
 */


/**
 * Default selector used by ProductAll
 */

const makeSelectProductAll = () => createSelector(
  selectProductAllDomain(),
  (substate) => substate.toJS()
);

export default makeSelectProductAll;
export {
  selectProductAllDomain,
};
