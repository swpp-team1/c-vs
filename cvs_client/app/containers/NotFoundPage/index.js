/**
 * NotFoundPage
 *
 * This is the page we show when the user visits a url that doesn't have a route
 */

import React from 'react';
import { FormattedMessage } from 'react-intl';
import Box from 'grommet/components/Box';
import CustomHeader from '../../components/CustomHeader';

import H1 from 'components/H1';
import messages from './messages';

export default function NotFound() {
  return (
    <article>
      <CustomHeader/>
      <Box align='center' alignContent='center'>
      <H1>
        <FormattedMessage {...messages.header} />
      </H1>
      </Box>
    </article>
  );
}
