<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/emcassi/resizer-py">
  </a>

<h1 align="center">Resizer-py</h1>

  <p align="center">
    Resize images with ease
    <br />
    <a href="https://github.com/emcassi/resizer-py"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/emcassi/resizer-py">View Demo</a>
    ·
    <a href="https://github.com/emcassi/resizer-py/issues">Report Bug</a>
    ·
    <a href="https://github.com/emcassi/resizer-py/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<br/>

<!-- ABOUT THE PROJECT -->
## About The Project
Resizer-py was built because I found it cumbersome to resize a group of images at once. This script allows you to resize any number of images to a given size in moments


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Pillow][Pillow]][Pillow-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* <a href="https://www.python.org/downloads/">Python</a>
* pip
  ```sh
  python -m ensurepip --upgrade
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/emcassi/resizer-py.git
   ```
2. Install required packages
   ```sh
   pip install pillow
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Using resizer-py is simple. Run the script from the command line using the following format

```s
(Resize all images in a directory) 
      python resize.py {width} {height} {directory}
      python resize.py {size} {directory}

(Resize a specific file)
      python resize.py {width} {height} {filename}
      python resize.py {size} {filename}

(Resize a collection of files)
      python resize.py {width} {height} {filename1} {filename2}
      python resize.py {size} {filename1} {filename2}
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@emcassi_](https://twitter.com/emcassi_) - alex.wayne.dev@gmail.com

Project Link: [https://github.com/emcassi/resizer-py](https://github.com/emcassi/resizer-py)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/emcassi/resizer-py.svg?style=for-the-badge
[contributors-url]: https://github.com/emcassi/resizer-py/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/emcassi/resizer-py.svg?style=for-the-badge
[forks-url]: https://github.com/emcassi/resizer-py/network/members
[stars-shield]: https://img.shields.io/github/stars/emcassi/resizer-py.svg?style=for-the-badge
[stars-url]: https://github.com/emcassi/resizer-py/stargazers
[issues-shield]: https://img.shields.io/github/issues/emcassi/resizer-py.svg?style=for-the-badge
[issues-url]: https://github.com/emcassi/resizer-py/issues
[license-shield]: https://img.shields.io/github/license/emcassi/resizer-py.svg?style=for-the-badge
[license-url]: https://github.com/emcassi/resizer-py/blob/master/LICENSE.txt
[Pillow]: https://img.shields.io/badge/pillow-000000?style=for-the-badge&logo=python&logoColor=white
[Pillow-url]: https://nextjs.org/