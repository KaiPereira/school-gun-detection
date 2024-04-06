import { MongoClient } from 'mongodb';

// MongoDB connection URI
const uri = '';
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

export default async function handler(req, res) {
    // Connect to MongoDB
    try {
        await client.connect();

        // Select the appropriate database and collection
        const database = client.db('mydatabase');
        const collection = database.collection('calls');

        // Query to retrieve all documents
        const documents = await collection.find({}).toArray();

        // Close the connection
        await client.close();

        // Send the retrieved documents as response
        res.status(200).json(documents);
    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
}