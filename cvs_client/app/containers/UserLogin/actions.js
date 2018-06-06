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
  SIGNUP_SUCCEEDED,
  LOGOUT
} from './constants';

export function defaultAction() {
  return {
    type: DEFAULT_ACTION,
  };
}

export function loginRequest (username, password) {
  return {
    type: LOGIN_REQUEST,
    username,
    password,
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
