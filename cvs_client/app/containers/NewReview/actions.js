/*
 *
 * NewReview actions
 *
 */

import {
  SEND_REQUEST_POST,
  DEFAULT_ACTION
} from './constants';

export function sendRequestPost (review, posts) {
  return {
    type: SEND_REQUEST_POST,
    review,
    posts
  }
}

export function defaultAction() {
  return {
    type: DEFAULT_ACTION,
  };
}
