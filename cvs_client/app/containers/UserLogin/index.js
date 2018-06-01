/*
 *
 * UserLogin
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Helmet from 'react-helmet';
import { FormattedMessage } from 'react-intl';
import { createStructuredSelector } from 'reselect';
import makeSelectUserLogin from './selectors';
import messages from './messages';
import Grommet from 'grommet'

export class UserLogin extends React.Component { // eslint-disable-line react/prefer-stateless-function
  render() {
    return (
      <Grommet.LoginForm title='로그인' onSubmit={() => console.log('login')} usernameType='text'/>
    );
  }
}

UserLogin.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

const mapStateToProps = createStructuredSelector({
  UserLogin: makeSelectUserLogin(),
});

function mapDispatchToProps(dispatch) {
  return {
    dispatch,
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(UserLogin);
