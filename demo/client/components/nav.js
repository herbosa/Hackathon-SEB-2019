import React, { Component } from 'react'
import { Embed, Image, Divider, Header, Segment, Reveal, Icon, Grid } from 'semantic-ui-react'


export default class NavBar extends Component {
  render() {
    return (
      <div>
          <Grid columns={1} textAlign="center">
            <Image size="small" src="/static/images/logo.png"></Image>
          </Grid>
      </div>
    )
  }
}
