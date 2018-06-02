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
import Box from 'grommet/components/Box';
import CustomHeader from '../../components/CustomHeader'

export class UserLogin extends React.Component { // eslint-disable-line react/prefer-stateless-function
  render() {
    return (
      <Grommet.App>
      <CustomHeader />
      <Box align='center' pad='large'>
      <Grommet.LoginForm align='center' title='C:VS login' onSubmit={() => console.log('login')} usernameType='text'/>
      </Box>
      </Grommet.App>
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
