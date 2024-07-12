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
    title: 'Boost your conversion rate',
    href: '#',
    description:
      "I've been using this knowledge base AI for a while now, and it has been incredibly helpful. The ability to upload files and chat with the AI makes it easy to find information quickly. The AI is also very responsive and provides accurate answers to my questions. Overall, a great tool for managing knowledge and improving productivity!",
    date: 'Mar 16, 2020',
    datetime: '2020-03-16',
    category: { title: 'Marketing', href: '#' },
    author: {
      name: 'Michael Foster',
      role: 'Co-Founder / CTO',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
  },
  {
    id: 2,
    title: 'Increase your website traffic',
    href: '#',
    description:
      ' This knowledge base AI is a game-changer! Being able to upload files and chat with the AI has made it so much easier to access information. The AI is smart and understands my queries, providing relevant answers in no time. It has definitely helped me become more efficient at work. Highly recommend!   ',
    date: 'Mar 10, 2020',
    datetime: '2020-03-10',
    category: { title: 'SEO', href: '#' },
    author: {
      name: 'Sylvia Hale',
      role: 'Co-Founder / CEO',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1552058544-f2b08422138a?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
  },
  {
    id: 3,
    title: 'Optimize your social media strategy',
    href: '#',
    description:
      "I can't imagine managing my documents without this knowledge base AI. Uploading files and chatting with the AI feels like having a personal assistant. It's so intuitive and saves me a lot of time searching for information. The AI's ability to understand complex queries is impressive. It's a must-have tool for anyone looking to streamline their knowledge management process!.",
    date: 'Feb 23, 2020',
    datetime: '2020-02-23',
    category: {
      title: 'Social Media',
      href: '#',
    },
    author: {
      name: 'Bradley Hunter',
      role: 'Marketing Specialist',
      href: '#',
      imageUrl:
        'https://images.unsplash.com/photo-1552058544-f2b08422138a?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',
    },
  },
  // More posts...
];

export { solutions, callsToAction, navigation, posts, products };
