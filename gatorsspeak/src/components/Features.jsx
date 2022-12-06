import React from 'react'
import {useState} from 'react'
import { flags } from '../constants'
import './Features.css'
import {groupOfKids} from '../assets'
const Features = () => {
  return (
  <div id='features'>
    <div id='variety'>
      <img id='diff-speakers' src={groupOfKids}></img>
      <div id='features-copy'>
        <p id='variety-copy'>
          A Variety Of Languages To Learn!
        </p>
        <p id='kids-copy'>
          Kids can learn English, Spanish, and more!
        </p>
      </div>
    </div>
    <div id='flags'>
      {flags.map((flag, index) => (
        <div key={flag.id} className='flag'>
          <p>{flag.content}</p>
          <img src={flag.icon} className='flag-icon'></img>
        </div>
      ))}
    </div>
  </div>
  )
}

export default Features