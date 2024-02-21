import React from 'react';
import TreeMap from 'react-d3-treemap';
import 'react-d3-treemap/dist/react.d3.treemap.css';
import jsonData from './assets/technology_top10.json';

interface TreeMapInputData {
  name: string;
  value?: number;
  children?: TreeMapInputData[];
}

export default class App extends React.Component<{}, { data: TreeMapInputData }> {
  constructor(props: {}) {
    super(props);
    this.state = {
      data: {
        name: 'Technology',
        children: this.parseData(jsonData),
      },
    };
  }

  parseData(data: any[]): TreeMapInputData[] {
    return data.map((item, index) => ({
      name: item.name,
      value: item.value,
      children: item.children ? this.parseData(item.children) : undefined,
    }));
  }

  render() {
    return (
      <div className="div-style">
        <TreeMap<TreeMapInputData>
          nodeStyle={{
            fontSize: 12,
            paddingLeft: 10,
            stroke: 'transparent !important',
            alignSelf: 'center !important',
            alignContent: 'center !important',
          }}
          data={this.state.data}
        />
      </div>
    );
  }
}



 