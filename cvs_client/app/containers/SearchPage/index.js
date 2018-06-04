/*
 *
 * SearchPage
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Helmet from 'react-helmet';
import { FormattedMessage } from 'react-intl';
import { createStructuredSelector } from 'reselect';
import makeSelectSearchPage from './selectors';
import messages from './messages';
import CustomHeader from '../../components/CustomHeader'
import Box from 'grommet/components/Box';
import Search from 'grommet/components/Search';
import MediaQuery from 'react-responsive';
import Article from 'grommet/components/Article';
import Section from 'grommet/components/Section';

export class SearchPage extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor(props){
    super(props);

    this.state = {term: ''};
    this.onInputChange = this.onInputChange.bind(this);
    this.onEnter = this.onEnter.bind(this);
  }

  onInputChange(event){
    this.setState({term: event.target.value});
    console.log(event.target.value);
    //this.props.searchProduct(this.state.term);
  }

  onEnter(item, selected){
    if(!selected){
      this.props.router.push(`/search/${this.state.term}`)
    }
  }
  
  render() {
    return (
      <div>
        SEARCH KEYWORD : {this.props.params.id}
        <Article>
          <CustomHeader/>
            <Box direction='row' justify='center' align='center'>
              <Section align='center' style={{alignItems: 'center', justifyContent: 'center', height: 100}}>

        <Box colorIndex='light-1' style={{margin: '20px 0px'}}>
        <MediaQuery query="(min-device-width: 1024px)">
        <Search style={{width: '700px'}} inline={true} placeHolder='검색' value={this.state.term} onDOMChange={this.onInputChange} 
        onSelect={this.onEnter} suggestions={['Suggestion is not yet implemented.']}/>
        </MediaQuery>
        <MediaQuery query="(max-device-width: 1023px)">
        <Search inline={true} placeHolder='검색' />
        </MediaQuery>
        </Box>
        </Section>
        </Box>
        </Article>

      </div>
    );
  }
}

SearchPage.propTypes = {
  dispatch: PropTypes.func.isRequired,
};

const mapStateToProps = createStructuredSelector({
  SearchPage: makeSelectSearchPage(),
});

function mapDispatchToProps(dispatch) {
  return {
    dispatch,
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(SearchPage);
