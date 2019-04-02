import React from 'react'
import Link from 'next/link'
import {Helmet} from "react-helmet";
import { Embed, Image, Divider, Header, Segment, Reveal, Icon, Grid } from 'semantic-ui-react'
import '../static/css/index.css'
import NavBar from '../components/nav'
import TextInput from '../components/textbox'

const Home = () => (
  <div className='main-page'>
    <Helmet>
        <title>Accueil</title>
        <meta name="googlebot" content="noindex"/>

        <meta name="description" content="Accueil" />
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous"/>
		<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
			<link rel="shortcut icon" href="../static/favicon.ico" type="image/x-icon"/>
			<link rel="icon" href="../static/logo.png" type="image/png"/>
      <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css"/>
    </Helmet>
    <NavBar/>
    <TextInput/>
    <Grid columns={7}>
    <Grid.Column width={2}></Grid.Column>
      <Grid.Column width={3}>
      <iframe src="https://calendar.google.com/calendar/b/2/embed?showNav=0&amp;showDate=0&amp;showPrint=0&amp;showTabs=0&amp;showCalendars=0&amp;showTz=0&amp;mode=WEEK&amp;height=600&amp;wkst=2&amp;bgcolor=%23ffffff&amp;src=alexandre.vokil%40gmail.com&amp;color=%231B887A&amp;ctz=Europe%2FParis" style={{borderWidth:0}} width="100%" height="600" frameborder="0" scrolling="no"></iframe>      </Grid.Column>
      <Grid.Column width={1}></Grid.Column>
      <Grid.Column width={3}>
      <iframe src="https://calendar.google.com/calendar/b/1/embed?showNav=0&amp;showDate=0&amp;showPrint=0&amp;showTabs=0&amp;showCalendars=0&amp;showTz=0&amp;mode=WEEK&amp;height=600&amp;wkst=2&amp;bgcolor=%23FFFFFF&amp;src=tristan.stavislas%40gmail.com&amp;color=%231B887A&amp;ctz=Europe%2FParis" style={{borderWidth:0}} width="100%" height="600" frameborder="0" scrolling="no"></iframe>      </Grid.Column>
      <Grid.Column width={1}></Grid.Column>
      <Grid.Column width={3}>
      <iframe src="https://calendar.google.com/calendar/b/3/embed?showNav=0&amp;showDate=0&amp;showPrint=0&amp;showTabs=0&amp;showCalendars=0&amp;showTz=0&amp;mode=WEEK&amp;height=600&amp;wkst=2&amp;bgcolor=%23FFFFFF&amp;src=delarteroger%40gmail.com&amp;color=%231B887A&amp;ctz=Europe%2FParis" style={{borderWidth:0}} width="100%" height="600" frameborder="0" scrolling="no"></iframe>
      </Grid.Column>
      <Grid.Column width={1}></Grid.Column>
    </Grid>
    </div>
)
export default Home

