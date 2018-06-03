import { createSelector } from 'reselect';

/**
 * Direct selector to the productDetail state domain
 */
const selectProductDetailDomain = () => (state) => state.get('productDetail');

/**
 * Other specific selectors
 */


/**
 * Default selector used by ProductDetail
 */

const makeSelectProductDetail = () => createSelector(
  selectProductDetailDomain(),
  (substate) => substate.toJS()
);

export default makeSelectProductDetail;
export {
  selectProductDetailDomain,
};
