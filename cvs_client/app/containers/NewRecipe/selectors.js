import { createSelector } from 'reselect';

/**
 * Direct selector to the newRecipe state domain
 */
const selectNewRecipeDomain = () => (state) => state.get('newRecipe');

/**
 * Other specific selectors
 */


/**
 * Default selector used by NewRecipe
 */

const makeSelectNewRecipe = () => createSelector(
  selectNewRecipeDomain(),
  (substate) => substate.toJS()
);

export default makeSelectNewRecipe;
export {
  selectNewRecipeDomain,
};
