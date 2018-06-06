/*
 *
 * UserLogin actions
 *
 */

import {
  DEFAULT_ACTION,
  LOGIN_REQUEST,
  LOGIN_SUCCEEDED,
  SIGNUP_REQUEST,
  SIGNUP_RESULT,
  SET_ERROR_MESSAGE,
  LOGOUT
} from './constants';

export function defaultAction() {
  return {
    type: DEFAULT_ACTION,
  };
}

export function signupResult (succeeded, message) {
  return {
    type: SIGNUP_RESULT,
    succeeded: succeeded,
    message: message
  }
}

export function signupRequest (username, password, email) {
  return {
    type: SIGNUP_REQUEST,
    username,
    password,
    email
  }
}
