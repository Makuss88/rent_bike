/* tslint:disable */
// @ts-ignore
// @ts-nocheck
import React, { useState, useEffect } from 'react';
import { NextPage } from 'next';
import { Button } from '@material-ui/core';


class Home extends React.Component {
  state = {
    bikes: [],
    number: '',
    color: '',
    is_free: '',
    image: '',
  }

  componentDidMount(){
    fetch("http://127.0.0.1:8000/bikes/")
      .then((res) => {
          return res.json();
       })
      .then(response => {
        this.setState({
          bikes: response,
        })
      }
    )
  }

  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value });
  }

  handleSubmit = (event) => {
    event.preventDefault();
    const { color, image, is_free, number } = this.state;

      fetch('http://127.0.0.1:8000/bikes/', {
       method: 'post',
       headers: {'Content-Type':'application/json'},
       body: JSON.stringify({
          "number_bike": number,
          "color_bike": color,
          is_free,
          image,
       })

     });
   }


  render() {
    const { bikes } = this.state;

    console.log(bikes.results)

    if (bikes && bikes.results && bikes.results.length) {
        bikes.results.map((el) => console.log(el));
    }

    return (
      <>
        {bikes && bikes.results && bikes.results.length && bikes.results.map((bike, index) => {
          return (
            <p key={index}>{bike.number_bike}</p>
          )
        })
        }
        <p>dupa</p>

       <form onSubmit={this.handleSubmit}>
            <input name="number" placeholder="number" type="text" value={this.state.number} onChange={this.handleChange} />
            <input name="color" placeholder="color" type="text" value={this.state.color} onChange={this.handleChange} />
            <input name="is_free" placeholder="is free" type="text" value={this.state.is_free} onChange={this.handleChange} />
            <input name="image" placeholder="image" type="text" value={this.state.image} onChange={this.handleChange} />
          <input type="submit" value="Wyślij" />
      </form>

      </>
    )
  }
}

// const Home: NextPage = () => {
//
//   const [hasError, setErrors] = useState(false);
//   const [bikes, setBikes] = useState([]);
//
//   useEffect(() => {
//     async function fetchData() {
//       const res = await fetch("http://127.0.0.1:8000/bikes/");
//       res
//         .json()
//         .then(res => setBikes(res))
//         .catch(err => setErrors(err));
//     }
//
//     fetchData();
//   });
//
//   let myBikes;
//   if (bikes && bikes.length) {
//     myBikes = bikes.map((bike) => {
//     console.log('bike', bike)
//       return (
//         <p>{bike.number_bike}</p>
//       )
//     })
//   }
//
//
//   return (
//      <div>
//         {myBikes}
//         <Button href="/contact">
//            Contact page
//         </Button>
//     </div>
// );
// }

export default Home;