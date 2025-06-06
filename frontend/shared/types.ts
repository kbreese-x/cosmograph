export interface Node {
  id: string;
  [key: string]: any; // Allow any additional properties
}

export interface Link {
  source: string;
  target: string;
  [key: string]: any; // Allow any additional properties
}