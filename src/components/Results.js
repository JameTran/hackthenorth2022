import * as React from 'react'
import { Box, Center, ChakraProvider, Button, ButtonGroup, Stack, Image, IconButton, Heading } from '@chakra-ui/react'
import { useState } from 'react'
import { BsArrowLeftSquare } from 'react-icons/bs';

function Results({ status, setStatus }) {
  // 2. Wrap ChakraProvider at the root of your app
  return (
    <ChakraProvider>
    <Box bg='grey'> 
      <Center w='100vw' h='100vh'>
        <Box bg='#B5E4FE' w='35vw' h="95vh" p={4} color='#B5E4FE' borderRadius="10px" padding='0'>
          <Box bg='white' w='35vw' h="15vh" p={4} color='#B5E4FE' borderRadius="10px" fontSize='5xl' fontWeight='bold' >
            <Stack direction='row' p={2} align='center'>
              <IconButton fontSize='50px' bg='white' icon={<BsArrowLeftSquare/>} onClick={() => {setStatus('library');console.log('hi');}}/>
              <Box color="#B5E4FE" fontSize="30px" spacing='50%'>
                English Presentation <br/>
                April 21, 2010
              </Box>
            </Stack>
            <Box bg='white' w='30vh' h='10vh' vcolour='#B5E4FE' align='center' marginLeft='auto' marginRight='auto' marginTop='10px'>
              Results
            </Box>
            <Box bg='white' w='50vh' h='60vh' vcolour='#B5E4FE' align='center' marginLeft='auto' marginRight='auto' marginTop='30px' fontSize='15px'>
              <Heading> Summary </Heading>
              <br/>
              I’m a single woman with a list of reasons why you should date me ... <br/><br/>

              This is a poem about a girl who is trying to get a boy to notice 
              her ... <br/><br/>

              I am incredibly beautiful ...<br/><br/>

              The New York Times bought Wordle for $30,000,000 in late January ...<br/><br/>

              I’m funny, beautiful, and intelligent ...<br/><br/>

              I’m a person who has a lot of opinions ...<br/><br/>

              I’m a good student ...

            </Box>
          </Box>
        </Box>
      </Center>
    </Box>
    </ChakraProvider>

  )
  }

  export default Results;