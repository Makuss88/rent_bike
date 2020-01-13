import { NextPage } from 'next';
import Button from '../components/Button';


const Home: NextPage = () => (
     <div>
        <p>to jest frontend polaczony z next js zeby był server side rendering</p>
        <p>backend odpowiada za zapytania bazodanowe i stworzenie api i w sumie tyle</p>
        <Button href="/contact" isCircled variant="outlined" >Contact page</Button>
        <Button href="/contact" isCircled variant="contained" >Contact page</Button>
    </div>
);

export default Home;