/*
 *
 * Header
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import CustomHeader from 'components/CustomHeader'
import { loginRequest } from '../App/actions';


const mapStateToProps = (state) => {
  console.log(state)
  return ({
    loginResult: state.get('global').toJS().loginResult,
  })}

function mapDispatchToProps(dispatch) {
  return {
    loginRequest: (username, password) => dispatch(loginRequest(username, password))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(CustomHeader);
