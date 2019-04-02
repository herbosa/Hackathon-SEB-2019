import React, { Component } from 'react'
import { Button, Checkbox, Form, Input, Radio, Select, Image, TextArea, Grid, GridColumn, Header, Divider } from 'semantic-ui-react'
import '../static/css/index.css'
import axios from 'axios'

class TextInput extends Component {
    state = {text: "", object: "", from: "contact@epitarques.com", clickable: false}

    handleChange = (e, { name, value }) => this.setState({ [name]: value })

    submitMail = () => {
        const { text, object, from, clickable } = this.state

		this.setState({ clickable: true })

        fetch('http://localhost:8080/distribute/' + text + "/")
        .then(response => {
			console.log(response)
          })
          .catch(error => {
			this.setState({ clickable: false })
		})
        console.log(object, text, from);
    }

    render() {
        const { text, object, from, clickable } = this.state
        return (
            <Grid columns={1} textAlign="center" className="background">
            <Divider hidden/>
            <Grid.Column width={12}>
                <Form onSubmit={this.submitMail}>
                    <Form.Input placeholder='From' name='from' value={from} onChange={this.handleChange} />
                    <Form.Input placeholder='Object' name='object' value={object} onChange={this.handleChange} />
                    <Form.Field control={TextArea} placeholder='Email'  style={{ minHeight: 200 }} name='text' value={text} onChange={this.handleChange}/>
                    <Form.Button color={clickable ? 'green' : 'orange'} control={Button} animated style={{height: 70, width: 130}}>
                        <Button.Content visible >
                            <Header as="h3">
							Submit 
                            </Header>
                        </Button.Content>
                        <Button.Content hidden>
						{clickable ? 
							 <Header as="h3">
								Send
							</Header>
						 :
                        <Grid centered>
                            <Image src="/static/images/brain.svg" size="tiny"  />
                        </Grid>
						}
                        </Button.Content>
                </Form.Button>
                </Form>
                </Grid.Column>
        </Grid>
        )
    }
}

export default TextInput