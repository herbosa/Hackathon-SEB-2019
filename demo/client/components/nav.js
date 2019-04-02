import React, { Component } from 'react'
import { Embed, Image, Divider, Header, Segment, Reveal, Icon, Grid } from 'semantic-ui-react'


export default class NavBar extends Component {
  render() {
    return (
      <div>
        <Divider hidden></Divider>
        <Grid columns={1} textAlign="center">
            <Image size="tiny" src="/static/images/paperplane.svg"></Image>
          </Grid>
          <Divider hidden></Divider>
          <Grid columns={1} textAlign="center">
            <Image size="small" src="/static/images/logo.svg"></Image>
          </Grid>
          <Divider hidden></Divider>
          <Divider hidden></Divider>
      </div>
    )
  }
}
