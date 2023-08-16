import {ImHome} from 'react-icons/im';
import {RiComputerFill} from 'react-icons/ri';
import {FaMicrochip} from 'react-icons/fa';
import {FcAbout} from 'react-icons/fc';

// all the items that would go into the navbar
export const NavbarData = [
    {
        title: "Home",
        icon: <ImHome />,
        link: "/"
    },
    {
        title: "About",
        icon: <FcAbout />,
        link: "/about"
    },
 {/*   {
        title: "Software",
        icon: <RiComputerFill />,
        link: "/software"
    },
    {
        title: "Hardware",
        icon: <FaMicrochip />,
        link: "/hardware"
    }*/},
]