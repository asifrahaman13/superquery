import { MdOutlineEco } from 'react-icons/md';
import {
  SiMysql,
  SiMongodb,
  SiPostgresql,
  SiPinescript,
  SiNeo4J,
  SiSqlite,
} from 'react-icons/si';
const TITLE = {
  mysql: 'MySQL',
  postgres: 'Postgres',
  sqlite: 'SQLite',
  mongodb: 'MongoDB',
  pinecone: 'Pinecone',
  qdrant: 'Qdrant',
  neo4j: 'Neo4j',
} as const;

const ICONS = {
  mysql: SiMysql,
  postgres: SiPostgresql,
  sqlite: SiSqlite,
  mongodb: SiMongodb,
  pinecone: SiPinescript,
  qdrant: MdOutlineEco,
  neo4j: SiNeo4J,
} as const;

export interface Status {
  message: string;
  status: boolean;
}

export interface HistoryItem {
  message: string;
  messageFrom: string;
  sql_query?: string;
  answer_type?:
    | 'bar_chart'
    | 'line_chart'
    | 'pie_chart'
    | 'plain_answer'
    | 'table_response'
    | 'sql_query'
    | 'plain';
}

export interface RenderConversationProps {
  websocketRef: React.MutableRefObject<WebSocket | null>;
  texts: string[];
  status: Status;
  db: IconKey;
}

export interface IconComponentsProps {
  props: {
    slug: TitleKeys;
  };
}

export { TITLE, ICONS };
export type IconKey = keyof typeof ICONS;
export type TitleKeys = keyof typeof TITLE;
