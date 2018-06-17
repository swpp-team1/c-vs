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

export class RecipeDetail extends React.Component { // eslint-disable-line react/prefer-stateless-function
  render() {
    return (
      <div>
        <Helmet
          title="RecipeDetail"
          meta={[
            { name: 'description', content: 'Description of RecipeDetail' },
          ]}
        />
        <h1>{this.props.params.id}</h1>
        <FormattedMessage {...messages.header} />
      </div>
    );
  }
}

RecipeDetail.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

const mapStateToProps = createStructuredSelector({
  RecipeDetail: makeSelectRecipeDetail(),
});

function mapDispatchToProps(dispatch) {
  return {
    dispatch,
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(RecipeDetail);
