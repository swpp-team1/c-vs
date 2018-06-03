/*
 *
 * NewRecipe
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { FormattedMessage } from 'react-intl';
import { createStructuredSelector } from 'reselect';
import makeSelectNewRecipe from './selectors';
import messages from './messages';
import { requestProductList } from './actions'
import Search from 'grommet/components/Search'


export class NewRecipe extends React.Component { // eslint-disable-line react/prefer-stateless-function
  render() {
    console.log(this.props.productList)
    return (
      <div>
        <Search inline={true} onDOMChange={(event) => this.props.requestProductList(event.srcElement.value)} suggestions={this.props.productList && this.props.productList.map((item) => item.name)}/>
      </div>
    );
  }
}


const mapStateToProps = (state) => {
  return ({
    productList: state.get('newRecipe').toJS().productList,
  })}

function mapDispatchToProps(dispatch) {
  return {
    requestProductList: (searchText) => dispatch(requestProductList(searchText)),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(NewRecipe);
