import { NextPage } from 'next';


const Home: NextPage<{ userAgent: string }> = ({ userAgent }) => (
     <div>
        <h1>Hello world! - user agent: {userAgent}</h1>
        <p>to jest frontend polaczony z next js zeby był server side rendering</p>
        <p>backend odpowiada za zapytania bazodanowe i stworzenie api i w sumie tyle</p>
    </div>
);

Home.getInitialProps = async ({ req }) => {
    const userAgent = req ? req.headers['user-agent'] || '' : navigator.userAgent;
    return { userAgent };
};


export default Home;