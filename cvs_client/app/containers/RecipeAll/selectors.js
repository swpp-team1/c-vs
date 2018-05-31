import { createSelector } from 'reselect';

/**
 * Direct selector to the recipeAll state domain
 */
const selectRecipeAllDomain = () => (state) => state.get('recipeAll');

/**
 * Other specific selectors
 */


/**
 * Default selector used by RecipeAll
 */

const makeSelectRecipeAll = () => createSelector(
  selectRecipeAllDomain(),
  (substate) => substate.toJS()
);

export default makeSelectRecipeAll;
export {
  selectRecipeAllDomain,
};
