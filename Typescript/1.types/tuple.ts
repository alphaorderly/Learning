
const person: {
    name: string,
    age: number,
    hobbies: string[],
    role: [number, string]
} = {
    name: 'Woo',
    age: 25,
    hobbies: ['Sports', 'Cooking'],
    role: [2, 'author']
}

let favoriteActivities: string[]
favoriteActivities = ['1', '2']  

for (const hobby of person.hobbies) {
    console.log(hobby)
}

