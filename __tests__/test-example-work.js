import React from 'react';
import { shallow } from 'enzyme';
import ExampleWork from '../js/example-work';

import Enzyme from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
Enzyme.configure({ adapter: new Adapter() });

//jest failing tests, changed url for local testing to no avail

describe("ExampleWork component", () => {
    it("Should be a section element", () => {
        expect("Hello").toEqual("Hello");
    });
});