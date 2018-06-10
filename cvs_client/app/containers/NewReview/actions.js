/*
 *
 * NewReview actions
 *
 */

import {
  SEND_REQUEST_POST,
  DEFAULT_ACTION,
  IS_SUCCESSFUL_POST
} from './constants';

export function sendRequestPost (review, posts) {
  return {
    type: SEND_REQUEST_POST,
    review,
    posts
  }
}

export function isSuccessfulPost (isSuccessful) {
  return {
    type: IS_SUCCESSFUL_POST,
    isSuccessful: isSuccessful
  }
}

export function defaultAction() {
  return {
    type: DEFAULT_ACTION,
  };
}
