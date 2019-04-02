import React, { Component } from 'react'
import { Button, Checkbox, Form, Input, Radio, Select, TextArea, Grid, GridColumn, Header, Divider } from 'semantic-ui-react'
import '../static/css/index.css'

class TextInput extends Component {
    state = {text: "", object: ""}

    handleChange = (e, { name, value }) => this.setState({ [name]: value })

    submitMail = () => {
        const { text, object } = this.state
        
        console.log(object, text);
    }

    render() {
        const { text, object } = this.state
        return (
            <Grid columns={1} textAlign="center" className="background">
            <Divider hidden/>
            <Grid.Column width={12}>
                <Form onSubmit={this.submitMail}>
                    <Form.Input placeholder='Object' name='object' value={object} onChange={this.handleChange} />
                    <Form.Field control={TextArea} placeholder='Email'  style={{ minHeight: 200 }} name='text' value={text} onChange={this.handleChange}/>
                    <Form.Button color="blue" control={Button}>Submit</Form.Button>
                </Form>
                </Grid.Column>
        </Grid>
        )
    }
}

export default TextInput