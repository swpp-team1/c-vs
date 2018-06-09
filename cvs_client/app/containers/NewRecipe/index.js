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
import { requestProductList, sendRequestPost } from './actions'
import Search from 'grommet/components/Search'
import Button from 'grommet/components/Button'
import List from 'grommet/components/List'
import ListItem from 'grommet/components/List'
import Image from 'grommet/components/Image'
import Heading from 'grommet/components/Heading';
import Title from 'grommet/components/Title';
import Form from 'grommet/components/Form';
import FormField from 'grommet/components/FormField';
import TextInput from 'grommet/components/TextInput';
import FormTrashIcon from 'grommet/components/icons/base/FormTrash'
import Edit from 'grommet/components/icons/base/Edit';

export class NewRecipe extends React.Component { // eslint-disable-line react/prefer-stateless-function
  constructor(props) {
    super(props)
    this.state = {
      selectedItem: null,
      searchText: '',
      selectedItems: [],
      recipeTitle:''
    }
    this.onSearchInputChange = this.onSearchInputChange.bind(this);
    this.onClickDelete = this.onClickDelete.bind(this);
  }

  onSearchInputChange(event){
      this.props.requestProductList(event.target.value)
      this.setState({searchText: event.target.value, selectedItem: null})
  }

  onClickDelete(item){
    console.log("clicked!", item)
    console.log(this.state.selectedItems);
    this.setState({selectedItems: this.state.selectedItems.filter(function(list) {
      return list !== item
  })});
  }


  render() {
    var searchSuggestion;
    if(this.props.productList !== undefined){
      searchSuggestion = this.props.productList.results && this.props.productList.results.slice(0,10).map((item) => item.name)
    }
    else{
      searchSuggestion=[];

    }
    console.log("recipe title:", this.state.recipeTitle)
    console.log("suggestion:",searchSuggestion)
    console.log("SEL ITEM:",this.state.selectedItems)
    return (
      <div>
        <Heading tag='h2'>새 레시피 작성</Heading>
        <Title>레시피 제목</Title>
        <Form>
          <FormField label="레시피 제목을 작성해주세요"><TextInput value={this.state.recipeTitle} onDOMChange={(event) => this.setState({recipeTitle: event.target.value})}/></FormField>
          <Title>재료 추가하기</Title>
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
                    <Button onClick={() => this.onClickDelete(item)}><FormTrashIcon/></Button>
                  </ListItem>
                )
              })
            }
          </List>
          <Title>만드는 법 작성</Title>
          <input id='image-input' type='file' onChange={(e) => console.log(e.target.files[0])}/>
        <Button icon={<Edit />}
          label='레시피 저장'
          onClick={() => {
            let nameChangedFile = new File([document.getElementById('image-input').files[0]], 'image-name')
            this.props.sendRequestPost(nameChangedFile)
          }}
          type='button'
          //type submit
          primary={true} />
        </Form>
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
    sendRequestPost: (post) => dispatch(sendRequestPost(post))
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(NewRecipe);
