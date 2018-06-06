/*
 *
 * SearchPage
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import Helmet from 'react-helmet';
import {bindActionCreators} from 'redux';
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
import { searchProduct, receivedSearchResult } from './actions';
import Heading from 'grommet/components/Heading';
import Card from 'grommet/components/Card';
import Tile from 'grommet/components/Tile';
import Tiles from 'grommet/components/Tiles';
import Image from 'grommet/components/Image';

export class SearchPage extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor(props){
    super(props);

    this.state = {term: '', result: []};
    this.onInputChange = this.onInputChange.bind(this);
    this.onEnter = this.onEnter.bind(this);
  }

  componentWillMount(){
    console.log("PARAM ID:", this.props.params.id);
    if(this.props.params.id === undefined){
      console.log("UNDEFINED PARAMETER ID")
    }
    else{
      console.log("PARAM: ", this.props.params.id);
      this.props.searchProduct(this.props.params.id);
    }

  }

  onInputChange(event){
    this.setState({term: event.target.value});
    console.log(event.target.value);
  }

  onEnter(item, selected){
    if(!selected){
      this.props.router.push(`/search/${this.state.term}`)
      location.reload();
    }
  }

  render() {
    var resultCard;
    if(this.props.searchResult == undefined) {
      resultCard = (<p>NO RESULT</p>);
    }
    else{
      console.log(this.props.searchResult.results)
      resultCard = this.props.searchResult.results.map((object, index) => {
      return (<Tile pad='medium' key={index}><Card colorIndex = 'light-1' textSize = 'small' thumbnail = {<Image src={object.image} />} label={object.manufacturer} heading = {object.name} key = {index} onClick={() => this.props.router.push(`/productDetail/${object.id}`)}/></Tile>);
    })
  }

    return (
      <div>
        SEARCH KEYWORD : {this.props.params.id}
        <Article>
          <Box direction='row' justify='center' align='center'>
            <Section align='center' style={{alignItems: 'center', justifyContent: 'center', height: 100}}>
              <Box colorIndex='light-1' style={{margin: '20px 0px'}}>
                <Heading margin='none' strong = {true} tag = 'h3'>제품 및 레시피 검색</Heading>
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
        <Box colorIndex='light-2'>
        <Tiles fill={true}>{resultCard}</Tiles>
        </Box>
      </div>
    );
  }
}


const mapStateToProps = (state) => {
  return ({
    searchResult: state.get('searchPage').toJS().searchResult
  })
}


function mapDispatchToProps(dispatch) {
  return { searchProduct: (searchKey) => dispatch(searchProduct(searchKey))}
}

export default connect(mapStateToProps, mapDispatchToProps)(SearchPage);
