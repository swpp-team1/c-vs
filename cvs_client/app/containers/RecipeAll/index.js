/*
 *
 * RecipeAll
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Helmet from 'react-helmet';
import { FormattedMessage } from 'react-intl';
import { createStructuredSelector } from 'reselect';
import makeSelectRecipeAll from './selectors';
import messages from './messages';
import CustomHeader from '../../components/CustomHeader';

export class RecipeAll extends React.Component { // eslint-disable-line react/prefer-stateless-function
  render() {
    return (
      <div>
        <CustomHeader/>
        <Helmet
          title="RecipeAll"
          meta={[
            { name: 'description', content: 'Description of RecipeAll' },
          ]}
        />
        <FormattedMessage {...messages.header} />
      </div>
    );
  }
}

RecipeAll.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

const mapStateToProps = createStructuredSelector({
  RecipeAll: makeSelectRecipeAll(),
});

function mapDispatchToProps(dispatch) {
  return {
    dispatch,
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(RecipeAll);
