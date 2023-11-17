<script lang="ts">
import axios from 'axios'

interface MyObject {
    src: any;
    alt: string;
  }

export default {
  data() {
    return {
      windowWidth: window.innerWidth,
      currentArr: [] as MyObject[],
      recordingInProgress: false,
     }
  },
  mounted() {
  },
  beforeDestroy() { 
    window.removeEventListener('resize', this.onResize); 
  },
  methods: {
    onRecording() {
      // recording
      // create an audio file and put audio here.
      this.recordingInProgress = true;
    },
    onRecordingStop() {
      // stop recording
      // try to set on upclick i.e hold to record
      this.recordingInProgress = false;
    },
    clearChatHistory() {
      // clears chat history
    },
    sendRecording(file) {
      // send recent recording to chatgpt
    },
    getChatGPTResponse() {
      // get response from chatgpt with fetch here
      // also think of cleanup if chat is long audio logs will build up
    },
    onResize() {
      this.windowWidth = window.innerWidth
    },
    fetchData() {
      axios.get('http://localhost:5000/api/data')
        .then(response => {
          console.log(response.data);
          // do something with response.data
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
  };
</script>

<template>
  <main>
    <html lang="en">
<body>
  
  <div class="portfolio-container">
    <div style=" background: #777069; display: flex; flex-direction: column; height: 100vh; overflow-y: scroll; overflow-x:hidden;">
      <div style="display:flex; height: 90%; width: 90%; margin-left: 5%; margin-top: 2.5%; gap: 2%;">
        <div class="flex-half">1</div>
        <div class="flex-half">2</div>

      </div>
   </div>
</div>

</body>
</html>
  </main>
</template>
<style lang="scss">
body,
html {
  height: 100%;
  background: #110101;
  overflow: hidden;
}
a {color:#fff;}
a:visited {color:#777069;}

.flex-half {
  flex: 30; background: #fff; width: 100%; height: 100%;
  display: flex; flex-direction: column;
  justify-content: flex-start; gap: 0;
}

.portfolio-container {
  height:100%; width: 100%; display: flex; flex-direction: column; overflow:hidden;
}

.portfolio-header {
  // background-color: rgba(10, 4, 0, 0.5);
  position: relative;
  color:white; display: flex; flex-direction:row; height: 48vh;
}

.transparent-background {
  background:rgb(118, 90, 63);
  opacity: 0.5;
}

.project-container {
  display: flex; flex-direction: row; justify-content: space-between; gap: 5vw; margin-top: 2%; margin-bottom: 2%; width: 90%; margin-left: auto; margin-right: auto; font-size: 1.3rem; height: 60vh;
}

.project-image-position {
  z-index: 5; height: 75%; width: 80%; position: absolute; bottom: -5%; right: -3%;
}

.project-gradient-square-size {
  position:absolute; flex: 40; height: 100%; width: 100%;
}

.project-image-container {
  flex:40; position:relative; height: 90%; width: 100%;
}

.project-text-container {
  display: flex; flex-direction: column; justify-content: space-between; flex: 60;
}

@media (max-width: 1360px) {
  .project-container {
  display: flex; flex-direction: column; justify-content: space-between; gap: 5vw; margin-top: 2%; margin-bottom: 2%; width: 80%; margin-left: auto; margin-right: auto; font-size: 1.3rem; height: 100rem;
}

.project-image-container {
  position:relative; border: 1px solid red; height: 90rem; width: 100%; display:block;
}

.project-text-container {
  display: flex; flex-direction: column; justify-content: space-between;
}

.project-image-position {
  z-index: 5; height: 90%; width: 80%; position: absolute; bottom: -5%; right: -3%;
}
  }
.split-slideshow {
  position: relative;
}
// under 1260
// portfolio CSS
.justify-around{	justify-content: space-around}
.flex-wrap	{flex-wrap: wrap}
#myImg {
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 100; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.9); /* Black w/ opacity */
}

/* Modal Content (image) */
.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
}

/* Caption of Modal Image */
#caption {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
  text-align: center;
  color: #ccc;
  padding: 10px 0;
  height: 150px;
}

@media screen and (min-width: 800px) {
  .caption {
  display:inline;
  }
}

/* Add Animation */
.modal-content, #caption {  
  -webkit-animation-name: zoom;
  -webkit-animation-duration: 0.6s;
  animation-name: zoom;
  animation-duration: 0.6s;
}

#myImg:hover {opacity: 0.7;}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
  z-index: 99;
}

.close:hover,
.close:focus {
  color: #bbb;
  text-decoration: none;
  cursor: pointer;
}

.show-small-screen {
  display: none;
}

.center-header{
  left:calc(100vw/2.2)!important;
}

.caption {
  position:absolute; right: 10%; top: 30%;
}


@media only screen and (max-width: 1300px){
  .caption {
  position:absolute; right: 10%; top: 5%;
}

.modal-content {
  margin: auto;
  display: block;
  width: 85%;
  bottom: 5%;
  max-width: 700px;
}
  .hide-small-screen {
    display: none !important;
  }
  .show-small-screen {
  display: block;
}
.center-header{
  left:calc(100vw/2.5)!important;
}
}

@media only screen and (max-width: 800px){

  .link-arr {
    display: none !important;
  }

  .hide-small-screen {
    display: none !important;
  }

  .show-small-screen {
  display: block;
}

.center-header{
  left:calc(100vw/2.7)!important;
}

.modal-content {
  margin: auto;
  display: block;
  width: 85%;
  bottom: 20%;
  max-width: 500px;
}

.close {
  position: absolute;
  top: 15px;
  left: 40%;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
}

.caption {
  position:absolute; right: 10%; top: 15%;
}
}

@media only screen and (max-width: 500px){
  .center-header{
  left:calc(100vw/3.4)!important;
}

.modal-content {
  margin: auto;
  display: block;
  width: 85%;
  bottom: 20%;
  max-width: 500px;
}

.close {
  position: absolute;
  top: 15px;
  left: 40%;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  transition: 0.3s;
}
}

.portfolio-button {
  height: 2.5rem;
  width: auto;
  background: rgba(42,28,14, 1);
  color: white;
  border-radius: 0.2rem;
  font-size: 1.2rem;
  margin-left: auto;
  margin-right: auto;
  font-weight:600;
  letter-spacing:0.2em;
  padding-left: 0.3rem;
  padding-right: 0.3rem;
  border:none;
  cursor:pointer;
  transition: background-color 0.2s, transform 0.1s;
}

.portfolio-button:hover {
  background-color: #333; /* Slightly darker color on hover */
}

.portfolio-button:active {
  background-color: #222; /* Even darker color on button press */
  transform: translateY(2px); /* Slight vertical shift to simulate button press */
}

.h-5 {
  height: 5rem;
}

.w-5 {
  width: 5rem;
}

.h-3 {
  height: 3.5rem;
}

.w-3 {
  width: 3.5rem;
}

.h-2 {
  height: 2.5rem;
}

.w-2 {
  width: 2.5rem;
}

.filter-white{
  filter: invert(100%) sepia(4%) saturate(7482%) hue-rotate(233deg) brightness(113%) contrast(95%);
}

.color-overlay {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: rgba(42,28,14,.6);
    z-index: 20;
}

#thumbnail {
    position: absolute;
    top: calc(100vh/8)!important;
    // left:calc(100vw/5.9)!important;
    bottom: 0;
    right: 0;
    margin: 16 40 16 5;
}
</style>

