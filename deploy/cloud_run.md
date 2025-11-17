# Cloud Run Deployment Instructions (Placeholder)

1. Build Docker image:
   gcloud builds submit --tag gcr.io/PROJECT_ID/supportgen

2. Deploy to Cloud Run:
   gcloud run deploy supportgen \
       --image gcr.io/PROJECT_ID/supportgen \
       --platform managed \
       --allow-unauthenticated
