import React from 'react'
import {LanguageProgress} from './'
import { flags } from '../constants'
import {girl, gator, boy} from '../assets'
import './Dashboard.css'
const Dashboard = () => {
  return (
    <div id='dashboard-container'>
      <div id='languages-container'>
        {flags.map((flag) => (
          <div className='progress-background'>
            <LanguageProgress key={flag.id} flag={flag}/>
          </div>
        ))}
      </div>
      <div id='images-container'>
          <img id='girl' src={girl}></img>
          <img id='gator' src={gator}></img>
          <img id='boy' src={boy}></img>
      </div>
    </div>
  )
}

export default Dashboard