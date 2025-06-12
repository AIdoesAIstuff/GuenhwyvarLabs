FROM node:18-alpine as build
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:18-alpine
WORKDIR /app
COPY --from=build /app .
ENV PORT=3000
EXPOSE 3000
CMD ["node", "server.js"]
