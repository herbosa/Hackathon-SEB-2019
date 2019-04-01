import React from 'react'
import Link from 'next/link'
import {Helmet} from "react-helmet";
import { Embed, Image, Divider, Header, Segment, Reveal, Icon, Grid } from 'semantic-ui-react'
import '../static/css/index.css'
import NavBar from '../components/nav'

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
    </div>
)
export default Home

