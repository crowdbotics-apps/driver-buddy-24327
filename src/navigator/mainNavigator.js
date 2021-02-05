import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import UserProfile201308Navigator from '../features/UserProfile201308/navigator';
import Tutorial201307Navigator from '../features/Tutorial201307/navigator';
import NotificationList201279Navigator from '../features/NotificationList201279/navigator';
import Settings201278Navigator from '../features/Settings201278/navigator';
import Settings201270Navigator from '../features/Settings201270/navigator';
import UserProfile201268Navigator from '../features/UserProfile201268/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
UserProfile201308: { screen: UserProfile201308Navigator },
Tutorial201307: { screen: Tutorial201307Navigator },
NotificationList201279: { screen: NotificationList201279Navigator },
Settings201278: { screen: Settings201278Navigator },
Settings201270: { screen: Settings201270Navigator },
UserProfile201268: { screen: UserProfile201268Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
