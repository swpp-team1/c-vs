/*
 *
 * RecipeDetail
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Helmet from 'react-helmet';
import { FormattedMessage } from 'react-intl';
import { createStructuredSelector } from 'reselect';
import makeSelectRecipeDetail from './selectors';
import messages from './messages';
import {requestRecipeDetail} from './actions'

export class RecipeDetail extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor(props){
    super(props)

  }

  componentWillMount(){
    this.props.getRecipeDetail(this.props.params.id)
  }
  
  render() {
    console.log(this.props.RecipeDetail.recipeDetail)
    return (
      <div>
        <h1>ID: {this.props.params.id}</h1>
      </div>
    );
  }
}


const mapStateToProps = createStructuredSelector({
  RecipeDetail: makeSelectRecipeDetail(),
});

function mapDispatchToProps(dispatch) {
  return {
    getRecipeDetail: (id) => dispatch(requestRecipeDetail(id))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(RecipeDetail);
