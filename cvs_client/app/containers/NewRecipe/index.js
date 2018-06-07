/*
 *
 * NewRecipe
 *
 */

import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { FormattedMessage } from 'react-intl';
import { createStructuredSelector } from 'reselect';
import makeSelectNewRecipe from './selectors';
import messages from './messages';
import { requestProductList } from './actions'
import Search from 'grommet/components/Search'
import Button from 'grommet/components/Button'
import List from 'grommet/components/List'
import ListItem from 'grommet/components/List'
import Image from 'grommet/components/Image'

export class NewRecipe extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor(props) {
    super(props)
    this.state = {
      selectedItem: null,
      searchText: '',
      selectedItems: [],
    }
    this.onSearchInputChange = this.onSearchInputChange.bind(this)
  }

  onSearchInputChange(event){
      this.props.requestProductList(event.target.value)
      this.setState({searchText: event.target.value, selectedItem: null})
  }


  render() {
    var searchSuggestion;
    if(this.props.productList != undefined){
      searchSuggestion = this.props.productList.results && this.props.productList.results.slice(0,10).map((item) => item.name)
    }
    else{
      searchSuggestion=[];

    }
    console.log("suggestion:",searchSuggestion)
    console.log("SEL ITEM:",this.state.selectedItems)
    return (
      <div>
        <Search inline={true}
                value={(this.state.selectedItem) ? this.state.selectedItem[0].name : this.state.searchText}
                  onSelect={(item, selected) => {
                    if(selected)
                      this.setState({selectedItem: this.props.productList.results.filter((product) => product.name === item.suggestion)})
                }}
                onDOMChange={this.onSearchInputChange}
                suggestions={searchSuggestion}/>
        <Button plain={false} style={{borderColor: !this.state.selectedItem && 'gray'}} label={'ADD'} onClick={() => {
          if(this.state.selectedItem) {
            const array = (this.state.selectedItems.concat(this.state.selectedItem))
            this.setState({selectedItems: array.filter((item, i) => {
              return array.findIndex((item2) => {
                return item.id === item2.id;
              }) === i;
            })})}
        }}/>
        <List>
          {
            this.state.selectedItems.map((item, key) => {
              return (
                <ListItem key={key} separator='horizontal' style={{borderBottom: '0.5px solid black', padding: 3}}>
                  <Image style={{height: '50px', width: '50px'}} fit='contain' size='small' src={item.image}/>
                  <span>{item.name}</span>
                </ListItem>
              )
            })
          }
        </List>
      </div>
    );
  }
}


const mapStateToProps = (state) => {
  return ({
    productList: state.get('newRecipe').toJS().productList,
  })}

function mapDispatchToProps(dispatch) {
  return {
    requestProductList: (searchText) => dispatch(requestProductList(searchText)),
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(NewRecipe);
