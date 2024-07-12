import { PhoneIcon, PlayCircleIcon } from '@heroicons/react/20/solid';
import {
  ArrowPathIcon,
  ChartPieIcon,
  CursorArrowRaysIcon,
  FingerPrintIcon,
  SquaresPlusIcon,
} from '@heroicons/react/24/outline';
import { MdOutlineEco } from 'react-icons/md';
import {
  SiMongodb,
  SiMysql,
  SiNeo4J,
  SiPinescript,
  SiPostgresql,
  SiSqlite,
} from 'react-icons/si';

const solutions = [
  {
    name: 'Analytics',
    description: 'Get a better understanding of your traffic',
    href: '#',
    icon: ChartPieIcon,
  },
  {
    name: 'Engagement',
    description: 'Speak directly to your customers',
    href: '#',
    icon: CursorArrowRaysIcon,
  },
  {
    name: 'Security',
    description: "Your customers' data will be safe and secure",
    href: '#',
    icon: FingerPrintIcon,
  },
  {
    name: 'Integrations',
    description: 'Connect with third-party tools',
    href: '#',
    icon: SquaresPlusIcon,
  },
  {
    name: 'Automations',
    description: 'Build strategic funnels that will convert',
    href: '#',
    icon: ArrowPathIcon,
  },
];

const products = [
  {
    name: 'mysql',
    description: 'Chat with your MySQL database',
    href: '/dashboard/mysql',
    icon: SiMysql,
  },
  {
    name: 'postgres',
    description: 'Chat with your PostgreSQL database',
    href: '/dashboard/postgres',
    icon: SiPostgresql,
  },
  {
    name: 'sqlite',
    description: 'Chat with SQLite database',
    href: '/dashboard/sqlite',
    icon: SiSqlite,
  },
  {
    name: 'mongodb',
    description: 'Chat with your MongoDB database',
    href: '/dashboard/mongodb',
    icon: SiMongodb,
  },
  {
    name: 'pinecone',
    description: 'Chat with Pinecone vector database',
    href: '/dashboard/pinecone',
    icon: SiPinescript,
  },
  {
    name: 'qdrant',
    description: 'Chat with Qdrant vector database',
    href: '/dashboard/qdrant',
    icon: MdOutlineEco,
  },
  {
    name: 'neo4j',
    description: 'Chat with your Neo4j database',
    href: '/dashboard/neo4j',
    icon: SiNeo4J,
  },
];

const callsToAction = [
  {
    name: 'Watch demo',
    href: '#',
    icon: PlayCircleIcon,
  },
  {
    name: 'Contact sales',
    href: '#',
    icon: PhoneIcon,
  },
];

const navigation = [
  {
    name: 'Integrations',
    href: '#',
    solutions: products,
  },
];

const posts = [
  {
    id: 1,
    title: 'Enhance Your Data Analysis',
    href: '#',
    description:
      "I've been using this LLM-powered platform for data analysis, and it's incredibly effective. The ability to upload datasets and chat with the AI to get insights is a game-changer. The AI provides accurate and relevant answers to my queries, making data analysis much more efficient. Highly recommended for anyone looking to streamline their data workflows!",
    date: 'Mar 16, 2025',
    datetime: '2025-03-16',
    category: { title: 'Data Analysis', href: '#' },
    author: {
      name: 'Michael Foster',
      role: 'Data Scientist',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
  },
  {
    id: 2,
    title: 'Boost Your Research Efficiency',
    href: '#',
    description:
      "This LLM-powered chat platform has revolutionized the way I conduct research. Uploading my data and getting immediate insights from the AI has saved me a lot of time. The AI understands complex queries and provides detailed, accurate answers. It's an essential tool for any researcher aiming to increase productivity.",
    date: 'Mar 10, 2025',
    datetime: '2025-03-10',
    category: { title: 'Research', href: '#' },
    author: {
      name: 'Sylvia Hale',
      role: 'Research Analyst',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1552058544-f2b08422138a?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
  },
  {
    id: 3,
    title: 'Optimize Your Business Insights',
    href: '#',
    description:
      "This platform powered by LLMs has transformed how I obtain business insights. Uploading data and interacting with the AI to get detailed responses is like having an expert consultant available 24/7. It's intuitive, responsive, and has significantly improved the speed and accuracy of my business decision-making process. A must-have for any business professional!",
    date: 'Feb 23, 2025',
    datetime: '2025-02-23',
    category: {
      title: 'Business Intelligence',
      href: '#',
    },
    author: {
      name: 'Bradley Hunter',
      role: 'Business Analyst',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1552058544-f2b08422138a?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
  },
  // More posts...
];

export { solutions, callsToAction, navigation, posts, products };
