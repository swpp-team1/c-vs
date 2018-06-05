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
import Anchor from 'grommet/components/Anchor'
import Form from 'grommet/components/Form'
import FormField from 'grommet/components/FormField'
import TextInput from 'grommet/components/TextInput'

export class UserLogin extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor() {
    super()
    this.state = {
      needSignUp: false,
    }
  }
  render() {
    return (
      <div>
      <CustomHeader/>
      <Box align='center' pad='large'>
        <Grommet.LoginForm align='center' title='C:VS login' onSubmit={() => console.log('login')} usernameType='text'/>
        <Anchor label='회원이 아니신가요?' onClick={() => this.setState({needSignUp: true})}/>
        {
          this.state.needSignUp &&
          <Form>
            <FormField label='Username'>
              <TextInput/>
          </FormField>
            <FormField label='Password'>
              <TextInput/>
            </FormField>
            <FormField label='e-mail'>
              <TextInput/>
            </FormField>
          </Form>
        }
      </Box>
      </div>
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
