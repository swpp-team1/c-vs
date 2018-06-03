import { createSelector } from 'reselect';

/**
 * Direct selector to the userLogin state domain
 */
const selectUserLoginDomain = () => (state) => state.get('userLogin');

/**
 * Other specific selectors
 */


/**
 * Default selector used by UserLogin
 */

const makeSelectUserLogin = () => createSelector(
  selectUserLoginDomain(),
  (substate) => substate.toJS()
);

export default makeSelectUserLogin;
export {
  selectUserLoginDomain,
};
