import React from 'react'
import { ChakraProvider, Box, Center, Stack, Image, Button, Icon } from '@chakra-ui/react'
import { AiOutlinePlusSquare } from 'react-icons/ai'

const Library = ( { status, setStatus } ) => {
  return (
    <ChakraProvider>
    <Box bg='grey'> 
      <Center w='100vw' h='100vh'>
        <Box bg='#B5E4FE' w='35vw' h="95vh" p={4} color='#B5E4FE' borderRadius="10px" padding='0'>
          
        <Stack spacing={8} direction='column' align='center'>
          <Box bg='white' w='35vw' h="15vh" p={4} color='#B5E4FE' borderRadius="10px" align='center' fontSize='5xl' fontWeight='bold'>
            Library 
          </Box>
          <input type='file' style={{display: 'none'}} id='invisiclick'></input>
          <Button type="file" bg='white' textColor='#B5E4FE' w='85%' h='15vh' onClick={() => {
            // HERE GOES THE FILE INPUT AND API STUFF 
            const invisy = document.getElementById('invisiclick');
            invisy.click();

            invisy.addEventListener("change", () => {
                var myFiles = this.files;
            }, false);

            setStatus('results')
          }}>
              <AiOutlinePlusSquare fontSize="60px"/>
          </Button>
          <Button bg='white' textColor='#B5E4FE' w='85%' h='15vh' onClick={() => {setStatus('results')}}>
            <Stack direction='row' align='left' spacing='5%' w='100%'>
                <Image
                  align='left'
                  boxSize='100px'
                  objectFit='cover'
                  src='https://miro.medium.com/max/900/1*372yy0zVcEVB2cxq5DuaPw.png'
                  alt='Video 2'
                />
                <Box bg='white' w='65%' h='90%' maxWidth='65%' colour='#B5E4FE' align='left'>
                  April 21, 2010 <br/> 
                  History Presentation
                </Box>
                
              </Stack>
          </Button>
          <Button bg='white' textColor='#B5E4FE' w='85%' h='15vh' onClick={() => {setStatus('results')}}>
            <Stack direction='row' align='left' spacing='5%' w='100%'>
                <Image
                  align='left'
                  boxSize='100px'
                  objectFit='cover'
                  src='https://simg.nicepng.com/png/small/137-1379157_kristin-headshot-blond.png'
                  alt='Video 3'
                />
                <Box bg='white' w='65%' h='90%' maxWidth='65%' colour='#B5E4FE' align='left'>
                  March 27, 2010 <br/> 
                  English Presentation
                </Box>
                
              </Stack>
          </Button>
          <Button bg='white' textColor='#B5E4FE' w='85%' h='15vh' onClick={() => {setStatus('results')}}    >
            <Stack direction='row' align='left' spacing='5%' w='100%'>
                <Image
                  align='left'
                  boxSize='100px'
                  objectFit='cover'
                  src='https://static1.discoverdigitalphotography.com/wp-content/uploads/2011/portrait-photography-tips-for-making-people-look-their-best/portrait.jpg'
                  alt='Video 4'
                />
                <Box bg='white' w='65%' h='90%' maxWidth='65%' colour='#B5E4FE' align='left'>
                  Feburary 10, 2010 <br/> 
                  Science Presentation 
                </Box>
                
              </Stack>
          </Button>
        </Stack>
        </Box>
      </Center>
    </Box>
    </ChakraProvider>
  )
}

export default Library