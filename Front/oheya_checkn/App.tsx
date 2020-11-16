import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import { SafeAreaProvider, SafeAreaView } from "react-native-safe-area-context";
import { Text, StatusBar, Button, StyleSheet } from "react-native";
import Main from "./components/Main";
import HomeScreen from "./components/HomeScreen";
import InvoiceEditScreen from "./components/InvoiceEditScreen";
import SummaryScreen from "./components/SummaryScreen";

const Stack = createStackNavigator();
function RootStack() {
    return (
        <Stack.Navigator
            headerMode="none"
            initialRouteName="Home"
            screenOptions={{
                gestureEnabled: false,
                Title: "お部屋チェックン",
                headerStyle: {
                    backgroundColor: "#363"
                },
                headerTintColor: "#fff",
                headerTitleStyle: {
                    fontWeight: "bold"
                }
            }}
        >
            <Stack.Screen
                name="Home"
                component={Main}
                options={{ title: "お部屋チェックン" }}
            />
        </Stack.Navigator>
    );
}

export default function App() {
    return (
        <SafeAreaProvider>
            <NavigationContainer>
                <RootStack />
            </NavigationContainer>
        </SafeAreaProvider>
    );
}
