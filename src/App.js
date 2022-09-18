import * as React from 'react'
import { Box, Center, ChakraProvider, Button, ButtonGroup, Stack, Image, IconButton, Heading} from '@chakra-ui/react'
import { useState } from 'react';
import { BsArrowLeftSquare } from 'react-icons/bs'
import Library from './components/Library';
import Home from './components/Results';

function App() {
  const [status, setStatus] = useState('library')
  // 2. Wrap ChakraProvider at the root of your app
  return (
    <div>
      {status === 'library' ? <Library status={status} setStatus={setStatus}/> :
                              <Home status={status} setStatus={setStatus}/>}
    </div>
  )
}



export default App;